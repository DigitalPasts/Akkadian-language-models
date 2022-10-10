# Akkadian language models
 Akkadian language models initially trained on Neo-Assyrian letters using spacy. Currently the training corpus consists only of SAA 1, with additional Neo-Assyrian inscriptions annotated by Mikko Luukko et. al. 2020.

The SAA texts and metadata were scraped fromm Oracc using modified versions of scripts made by Niek Veldhuis (originals found at GitHub repository niekveldhuis/compass/2_1_Data_Acquisition_ORACC/).
The raw text files are in normalization, with one file per letter (save for the supplemental Neo-Assyrian royal inscriptions, which are bundled in one file). These files were then annotated in Inception for part of speech, syntactic structure, and morphology according to both the Universal Dependencies framework (universaldependencies.org) and conventions used in Luukko et. al. 2020.
The annotated files are in conllu format. The process of hand-annotation was assisted by bootstrapping. First, linguistic metadata culled from Oracc provided lemmas and coarse pos tags for most tokens, although these were occasionally changed by hand on linguistic grounds (see subfolder explanations) or overwritten by the language models in the course of training. Indeed, in the course of hand-annotation a spacy language model was periodically trained on the texts
annotated up till that point and then used to suggest annotations for the remaining raw texts. These suggestions were verified or corrected by hand in a portion of the remaining raw texts until the enlarged training set justified retraining the model. This process accelerated the speed of hand-annotation (human in the loop). 
Additional details on the bootstrapping process can be found in the respective subfolders.

This repository also contains a prototype Akkadian Language class designed for spacy 3.0. It is currently meant for normalized texts and contains a substantial list of tokenizer exceptions for proper nouns and noun phrases in construct. 


Works cited:

Mikko Luukko, Aleksi Sahala, Sam Hardwick, and Krister Lindén. 2020. Akkadian Treebank for early Neo-Assyrian Royal Inscriptions. In Proceedings of the 19th International Workshop on Treebanks and Linguistic Theories, pages 124–134, Düsseldorf, Germany. Association for Computational Linguistics.