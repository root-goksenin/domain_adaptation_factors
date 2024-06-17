# domain_adaptation_factors
This repository contains the code and data for paper : [url].


# How to Install 

The preffered way of installation is via github and poetry. If poetry does not exist in your environment you can install the repo with pip install as well.

1. 
```bash 
git clone https://github.com/root-goksenin/domain_adaptation_factors.git
```
2. ```bash
    poetry install
    poetry shell
```
If poetry is not available

```bash
    pip install -r requirements.txt
```


# How to Reproduce 

I have made all the data available under /data and /shared_json folders. Data folder contains the CSV files for the cleaned data, and /shared_json folder contains the 
json files for the raw data. 


If you wish to produce the raw data your own, you can use main_analyzer.py function with the following command

```bash
python3 main_analyzer.py --source_query_path {source_path}/{queries_file}.jsonl --source_corpus_path ../{source_path}/{corpus_file}.jsonl --test_query_path {test_path}/{queries_file}.jsonl --test_corpus_path .{test_path}/{corpus_file}.jsonl --generated_query_path {test_path}/{generated_queries_path}.jsonl 
```

For reproducing the BEIR and LoTTE experiments use msmarco dataset from BEIR as the source data. GPL and InPars generated queries are already provided by [URL] and [URL]. Download these and put it under the test path folders. The test path folders should be the ones from BEIR.
Later, you can put all these under a CSV file. 
For the Improvement in NDCG@10 see [URL] and [URL].

To reproduce the plots use

```bash
python3 main_plotter.py
```


