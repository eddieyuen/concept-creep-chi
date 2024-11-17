# concept_creep_chi
## Summary
This study examines the phenomenon of concept creep within the Chinese context and to explore how ideological factors may influence the semantic expansion of different domains of concept. By applying a diachronic word embedding approach on the Chinese People's Daily corpus, the research analyzes the semantic expansion of both harm-related and nationalism concepts concepts over the past few decades. The findings suggest that concept creep is not confined to the ideological left but is influenced by broader cultural and moral dynamics, particularly a heightened sensitivity to harm. 

## Research Questions
1. Is there evidence of concept creep across the ideological spectrum in the Chinese context, encompassing both harm-related and nationalism-related concepts?
2. How is the cultural salience of each moral foundation associated with the semantic breadth of harm-related and nationalism-related concepts in the Chinese context?

## Methods
- Word embeddings models for the corpus from 1979 to 2023 were trained using the word2vec algorithm in the ‘gensim’ package.
- Four harm-related concepts are selected as illustrative examples of the concept creep phenomenon in China: “prejudice,” “bullying,” “mental disorder,” and “trauma”.
- To explore whether concept creep extends outside of the political left, four nationalism-related concepts are chosen: “secession,” “conspiracy,” “sovereignty,” and “terrorism.”
- The semantic breadth of the target concepts in a year was quantified as the average cosine similarity of their contextualized representations.

## Analysis
- Examined the trend of semantic expansion by correlating the semantic breadth of the target concepts with year
- Examined the relationship between the cultural salience of moral foundations (harm, fairness, ingroup, authority, purity) and the semantic breadth of the target concepts using multivariate multiple regressions

## Results
- The results show significant semantic expansion for three harm-related concepts (prejudice, bullying, trauma) and two nationalism-related concepts (conspiracy, sovereignty), suggesting that concept creep occurs across the ideological spectrum.
- The cultural salience of the harm foundation is positively associated with the semantic breadth of these concepts, consistent with the idea that a heightened sensitivity to harm drives concept creep. 
