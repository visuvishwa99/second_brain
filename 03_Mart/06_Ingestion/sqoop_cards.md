TARGET DECK: SecondBrain::06_Ingestion

START
Cloze
To handle {data skew} in Sqoop, use hash-based splitting with the {--split-by} option.
<!--ID: 1770332603165-->
END

START
Cloze
For hash-based splitting in Sqoop, create a temporary column using hash functions like {MD5} or {SHA1} on the row content.
<!--ID: 1770332603168-->
END

START
Cloze
Sqoop distributes data across {mappers} based on the split column values.
<!--ID: 1770332603169-->
END

START
Cloze
When the default split column causes skew, try splitting by a column with {high cardinality} like telephone numbers.
<!--ID: 1770332603171-->
END

START
Cloze
A real-world Sqoop optimization reduced ingestion time from {17 hours} to {5 hours} by changing the split-by column from alphanumeric to telephone number.
<!--ID: 1770332603172-->
END
