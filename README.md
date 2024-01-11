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

This dataloader is tailored for use with C3DC.

### Transformation

UChicago provides JSON files that contain C3DC data. However, this dataloader reads from TSV files to load data into Neo4j. Therefore, we have some code in `/transformer` to transform the JSON files to TSV files.

Before running the transformation, place the JSON files in the `/data` directory. Then, to run the transformation, execute this command:

```bash
python transformer/transformer.py
```

The TSV files will be saved to `/data`.

### Neo4j

Configured by `/config/config.yml` and `/config/props-c3dc.yml`.

Load data from the TSV files into Neo4j with this command:

```bash
python loader.py config/config.yml
```

### Opensearch

Configured by `/config/es_indices_c3dc.yml` and `/config/es_loader.yml`.

Build Opensearch indices from Neo4j with this command:

```bash
python es_loader.py config/es_indices_c3dc.yml config/es_loader.yml
```

### Transformation Unit Tests

Run units tests on the transformation functionality with this command:

```bash
sh transformer-unit-tests.sh
```
