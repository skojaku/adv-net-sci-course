This dataset is compiled from http://ftp.cs.stanford.edu/pub/sgb/jean.dat compiled by  D. E. Knuth. See D. E. Knuth, 1993. The Stanford GraphBase: a platform for combinatorial computing, pp. 74-87. New York: AcM Press for details.

The original data is a single file containing two tables with different delimiters. The table is separated into `characters.csv` and `section_character_table.csv` with consistent delimiter `,`.

The section name was originally indicated in format `<section>.<subsection>.<subsubsection>`. In the new format, the section title is format by `<section>.<subsection><subsubsection>` where `subsection`and `subsubsection` are represented by two-digit number. For section number less than 10, a leading 0 is appended. For instance, the subsubsection 10 of subsection 2 of section 1 is represented by `1.0210`.
