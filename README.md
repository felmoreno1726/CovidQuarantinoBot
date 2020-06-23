# CovidQuarantinoBot
## Description
Covid Quarantino is a skill extensible friendly general purpose chatbot to be entertained with this quarantine.
## Results
See [report.pdf](results/acl_style_main.pdf) 
# Dependencies
#### Requires python >=3.6. Make sure that you have the latest version of pip installed
- To create a virtual environment with ` python3 -m venv venv`
- To activate the virtual environment ` source venv/bin/activate`
- To install dependencies run: ` pip install -r requirements.txt`
- Install and link spacy models
` python -m spacy download en_core_web_md `
` python -m spacy link en_core_web_md en `

# Running the chatbot
### Training
- Run ` rasa train`
### Testing
- Run `rasa test`
### Usage
- Run ` ./run.sh`
