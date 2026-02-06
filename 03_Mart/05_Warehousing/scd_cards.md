TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
{SCD Type 1} (Overwrite) replaces the old value with the new value, preserving {no history}.
<!--ID: 1770353415983-->
END

START
Cloze
{SCD Type 2} (Row Versioning) tracks full history by inserting a new row for every change and marking old rows as {expired} (using `is_current` or `end_date`).
<!--ID: 1770353415984-->
END

START
Cloze
{SCD Type 3} saves only the immediate last change by adding a {previous_value} column.
<!--ID: 1770353415986-->
END

START
Cloze
{Late Arriving Dimensions} occur when Fact data arrives before Dimension data; handled by inserting a {placeholder} row then updating it later.
<!--ID: 1770353415988-->
END

START
Cloze
In the Medallion Architecture, the {Silver} layer typically implements SCD Type 1 or 2 logic, while Bronze is raw append-only.
<!--ID: 1770353415989-->
END
