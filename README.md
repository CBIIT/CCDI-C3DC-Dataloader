# NCI C3DC Data Loader

This is the NCI C3DC Data Loader. It's based on the NCI ICDC/CTDC Data Loader (<https://github.com/CBIIT/icdc-dataloader>)

## Module List

The NCI C3DC Data Loader includes multiple data loading modules:

-   **Data Loader**
    -   The Data Loader module is a versatile Python application used to load data into a Neo4j database.
    -   [Data Loader Documentation](docs/data-loader.md)

-   **File Copier**
    -   The File Copier module copies files from a source URL to a designated AWS S3 Bucket.
    -   [File Copier Documentation](docs/file-copier.md)
    
-   **File Loader**
    -   The File Loader module processes incoming S3 files and then calls the Data Loader module to load the processed file data into a Neo4j database.
    -   [File Loader Documentation](docs/file-loader.md)
    
-   **Model Converter**
    -   The Model Converter uses a combination of YAML format schema files, a YAML formatted properties files, and a GraphQL formatted queries file to generate a GraphQL formatted schema.
    -   [Model Converter Documentation](docs/model-converter.md)

## Usage

This dataloader is tailored for use with C3DC. The ETL process consists of the following steps:

1. Download harmonized JSON files
2. Transform JSON files to TSV files
3. Load data from TSV files to Neo4j
4. Index data into Opensearch from Neo4j

### Transformation

UChicago provides JSON files that contain C3DC data. However, this dataloader reads from TSV files to load data into Neo4j. Therefore, we have some code in `/transformer` to transform the JSON files to TSV files.

Before running the transformation, place the JSON files in the `/data` directory. Each study should have its own folder, and then all the harmonized JSON files for a study should be in that study's folder. Here's an example directory structure:

```text
\data
├───phs000466
│       phs000466_discovery.harmonized.json
│
├───phs000467
│       phs000467_discovery.harmonized.json
│       phs000467_validation.harmonized.json
│
├───phs000468
│       phs000468_discovery.harmonized.json
│       phs000468_validation.harmonized.json
│
└───phs003519
        phs003519.harmonized.json
```

Then, to run the transformation, execute this command:

```bash
python transformer/transformer.py
```

The TSV files will be saved to `/data`. Log files are stored in `/tmp`, and the filename starts with "transformer-".

### Neo4j

Configured by `/config/config.yml` and `/config/props-c3dc.yml`.

Load data from the TSV files into Neo4j with this command:

```bash
python loader.py config/config.yml
```

Log files are stored in `/tmp`, and the filename starts with "Data_Loader-".

### Opensearch

Configured by `/config/es_indices_c3dc.yml` and `/config/es_loader.yml`.

Build Opensearch indices from Neo4j with this command:

Log files are stored in `/tmp`, and the filename starts with "bento-".

```bash
python es_loader.py config/es_indices_c3dc.yml config/es_loader.yml
```

### Transformation Unit Tests

Run units tests on the transformation functionality with this command:

```bash
sh transformer-unit-tests.sh
```

<!-- TODO: C3DC-1646 - Update backend API to include CPI synonym values in JSON output -->

<!-- TODO: C3DC-1646 - Update backend API to include CPI synonym values in JSON output -->
