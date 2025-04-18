name: Zip CSV files

on: [workflow_dispatch]

jobs:
  zip-csv:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Zip CSV files
        run: |
          cd workspaces/code2/Download_Batch_2
          zip csv_files.zip *.csv

      - name: Upload zipped file
        uses: actions/upload-artifact@v3
        with:
          name: csv-files-archive
          path: workspaces/code2/Download_Batch_2/csv_files.zip
