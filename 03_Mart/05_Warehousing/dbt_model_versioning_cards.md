TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
The main drawback of using a manual `var()` in `dbt_project.yml` for model versioning is that it is {manual/error-prone} and does not automatically track {upstream logic changes}.
END

START
Cloze
`dbt_artifacts` checksums are limited because they only track the hash of the {individual model file}, ignoring changes in {upstream dependencies/intermediate models}.
END

START
Cloze
To automatically track version changes based on the entire lineage (including upstream logic), you should use a {compile-time macro} that traverses the {graph nodes} to generate a composite hash.
END
