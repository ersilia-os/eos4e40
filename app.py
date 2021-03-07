import streamlit as st
import numpy as np
from ersilia.io.input import MoleculeInput
from ersilia.app import StreamlitBlocks
import eos0aaa as Model

MODEL_ID = "eos4e40"

sb = StreamlitBlocks(MODEL_ID)

sb.header()

"""

mdl = sb.load_model()

def load_model():
    mdl = Model.load()
    return mdl

inp = sb.molecule_input()

if inp != "":


mdl = load_model()

st.subheader("Input")

inp = st.text_input("Please enter a molecule (name, SMILES...)", value='', max_chars=None, key=None, type='default')

if inp != "":

    ci = MoleculeInput()
    smi = ci.single(inp)

    st.text("SMILES: %s" % smi)

    output = mdl.predict([smi])
    output = int(np.array(output)[0])

    if output == 0:
        text = "Inactive"
    else:
        text = "Active"

    del output

    st.subheader("Output")
    st.text(text)

"""