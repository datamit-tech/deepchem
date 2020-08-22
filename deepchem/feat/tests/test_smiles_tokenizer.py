# Requirements - transformers, tokenizers
import os
from unittest import TestCase
from deepchem.feat.smiles_tokenizer import SmilesTokenizer
from transformers import RobertaForMaskedLM


class TestSmilesTokenizer(TestCase):
  """Tests the SmilesTokenizer to load the USPTO vocab file and a ChemBERTa Masked LM model with pre-trained weights.."""


  def test_tokenize(self):
      vocab_path = os.path.join(os.path.dirname(__file__), "data", "vocab.txt")

      model = RobertaForMaskedLM.from_pretrained('seyonec/SMILES_tokenized_PubChem_shard00_50k')
      model.num_parameters()

      tokenizer = SmilesTokenizer(vocab_path, max_len=model.config.max_position_embeddings)
      print(tokenizer.encode("CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@](C#N)([C@H](O)[C@@H]1O)C1=CC=C2N1N=CN=C2N)OC1=CC=CC=C1"))

