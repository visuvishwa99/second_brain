#!/bin/bash
# run_audit.sh - Orchestrator for the Maintenance Agent
# Usage: bash scripts/run_audit.sh

echo "🔍 Starting Second Brain Audit..."
echo ""

# Step 1: Fast bash scan
echo "Step 1/2: Running bash scan..."
bash scripts/audit_brain.sh

# Step 2: Smart Python analysis
echo ""
echo "Step 2/2: Running duplicate detection..."
python scripts/audit_brain.py

echo ""
echo "✅ Audit complete! Review: agents/audit_report.md"
