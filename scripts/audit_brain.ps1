$BrainDir = "02_Brain"
$MartDir = "03_Mart"
$RawDir = "01_Raw\journals"
$ReportFile = "automation\audit_report.md"

$ReportContent = @()
$ReportContent += "# Audit Report - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
$ReportContent += ""
$ReportContent += "## Compliance Issues"
$ReportContent += ""

# --- 1. Stale Journals ---
$ReportContent += "### Stale Journals (unprocessed)"
$RawFiles = Get-ChildItem -Path $RawDir -Filter *.md -ErrorAction SilentlyContinue
foreach ($File in $RawFiles) {
    if (Select-String -Path $File.FullName -Pattern "processed: false" -SimpleMatch -Quiet) {
        $ReportContent += "- $($File.Name)"
    }
}
$ReportContent += ""

# --- 2. Brain Notes Missing Tags ---
$ReportContent += "### Brain Notes Missing Tags"
$BrainFiles = Get-ChildItem -Path $BrainDir -Filter *.md -Recurse | Where-Object { $_.Name -notlike "*_MOC.md" }
foreach ($File in $BrainFiles) {
    if (-not (Select-String -Path $File.FullName -Pattern "^tags:" -Quiet)) {
        $ReportContent += "- [NO_TAG] $($File.Name)"
    }
}
$ReportContent += ""

# --- 3. File Naming Violations ---
$ReportContent += "### File Naming Violations"
foreach ($File in $BrainFiles) {
    if ($File.Name -cmatch "[A-Z]") {
        $ReportContent += "- [UPPERCASE] $($File.Name) (filename should be lowercase)"
    }
}
$ReportContent += ""

# --- 4. Orphan Cards (Mart without Brain) ---
$ReportContent += "### Orphan Cards (Mart without Brain)"
$MartFiles = Get-ChildItem -Path $MartDir -Filter "*_cards.md" -Recurse
foreach ($CardFile in $MartFiles) {
    $BaseName = $CardFile.Name -replace "_cards.md", ""
    
    # Calculate relative path from MartDir
    $FullMartDir = (Get-Item $MartDir).FullName
    $CardDir = $CardFile.DirectoryName
    
    $RelPath = ""
    if ($CardDir.StartsWith($FullMartDir)) {
        $RelPath = $CardDir.Substring($FullMartDir.Length)
        if ($RelPath.StartsWith("\")) { $RelPath = $RelPath.Substring(1) }
    }
    
    # Construct expected Brain path
    $BrainFile = ""
    if ([string]::IsNullOrEmpty($RelPath)) {
         $BrainFile = Join-Path -Path $BrainDir -ChildPath "$BaseName.md"
    } else {
         $PathWithSubdir = Join-Path -Path $RelPath -ChildPath "$BaseName.md"
         $BrainFile = Join-Path -Path $BrainDir -ChildPath $PathWithSubdir
    }

    if (-not (Test-Path $BrainFile)) {
         $ReportContent += "- [ORPHAN] $($CardFile.Name) (missing: $BrainFile)"
    }
}
$ReportContent += ""

# --- 5. Brain Notes without Cards ---
$ReportContent += "### Brain Notes without Cards"
foreach ($BrainFile in $BrainFiles) {
    $BaseName = $BrainFile.Name -replace ".md", ""
    
    # Calculate relative path from BrainDir
    $FullBrainDir = (Get-Item $BrainDir).FullName
    $BrainFileDir = $BrainFile.DirectoryName
    
    $RelPath = ""
    if ($BrainFileDir.StartsWith($FullBrainDir)) {
        $RelPath = $BrainFileDir.Substring($FullBrainDir.Length)
        if ($RelPath.StartsWith("\")) { $RelPath = $RelPath.Substring(1) }
    }
    
    # Construct expected Card path
    $CardFile = ""
    if ([string]::IsNullOrEmpty($RelPath)) {
         $CardFile = Join-Path -Path $MartDir -ChildPath "${BaseName}_cards.md"
    } else {
         $PathWithSubdir = Join-Path -Path $RelPath -ChildPath "${BaseName}_cards.md"
         $CardFile = Join-Path -Path $MartDir -ChildPath $PathWithSubdir
    }
    
    if (-not (Test-Path $CardFile)) {
        $ReportContent += "- [NO_CARDS] $($BrainFile.Name)"
    }
}
$ReportContent += ""

# --- 7. Consolidation Candidates ---
$ReportContent += "### Consolidation Candidates"
foreach ($File in $BrainFiles) {
    $LineCount = (Get-Content $File.FullName | Measure-Object).Count
    if ($LineCount -lt 15) {
        $ReportContent += "- [SMALL_FILE] $($File.Name) ($LineCount lines) -> Consider merging"
    }
    if ($File.Name -match "\d{4}-\d{2}-\d{2}") {
        $ReportContent += "- [DATED_FILE] $($File.Name) -> Consider merging"
    }
}
$ReportContent += ""

# --- Summary ---
$ReportContent += "## Summary"
$ReportContent += "- Brain Notes: $($BrainFiles.Count)"
$ReportContent += "- Mart Cards: $($MartFiles.Count)"
$ReportContent += "- Raw Journals: $($RawFiles.Count)"
$ReportContent += ""
$ReportContent += "---"
$ReportContent += "## Next Steps"
$ReportContent += "1. Review flagged duplicates and merge if appropriate"
$ReportContent += "2. Add missing tags to Brain notes"
$ReportContent += "3. Generate cards for Brain notes without them"
$ReportContent += "4. Process stale journals in 01_Raw"
$ReportContent += ""
$ReportContent += "> This report is **read-only**. No files were modified."
$ReportContent += "> **Note:** Duplicate detection was SKIPPED because Python is not available in this environment."

$ReportContent | Out-File -FilePath $ReportFile -Encoding utf8
Write-Host "Audit report generated at $ReportFile"
