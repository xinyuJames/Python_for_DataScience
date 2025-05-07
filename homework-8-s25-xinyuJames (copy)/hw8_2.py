import numpy as np
from helper import remove_punc
from hw8_1 import *
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords


# Clean and prepare the contents of a document
def read_and_clean_doc(doc):
    
    '''
    Arguments:
        doc: string, the name of the file to be read.
    Returns:
        all_no_stop: string, a string of all the words in the file, with stopwords removed.
    Notes: Do not append any directory names to doc -- assume we will give you a string representing a file name that will open correctly
    '''     
    
    # 1. Open document, read text into *single* string
    with open(doc, "r") as f:
        allStr = f.read()

    # 2. Filter out punctuation from list of words (use remove_punc)
    all_rm_punc = remove_punc(allStr)

    # 3. Make the words lower case
    all_lower = all_rm_punc.lower()

    # 4. Filter out stopwords
    tok_low = all_lower.split(" ")
    filt_tok = [tok for tok in tok_low if tok not in stopwords.words("english")]
    all_no_stop = "".join(filt_tok)

    return all_no_stop


# Builds a doc-word matrix
def build_doc_word_matrix(doclist, n, normalize=False):
    
    '''
    Arguments:
        doclist: list of strings, each string is the name of a file to be read.
        n: int, the length of each n-gram
        normalize: boolean, whether to normalize the doc-word matrix
    Returns:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents,
            with one row per document and one column per ngram (there should be as many columns as unique words that appear across *all* documents. 
            Also, Before constructing the doc-word matrix, you should sort the list of ngrams output and construct the doc-word matrix based on the sorted list
        ngramlist: list of strings, the list of ngrams that correspond to the columns in docword
    '''
    # TODO: complete the function



    docword, ngramlist = None, None
    cleaned_docs = []
    ngram_docs = set()
    for doc in doclist:
        cleaned = read_and_clean_doc(doc)
        cleaned_docs.append(cleaned)
        ngram_docs.update(get_ngrams(cleaned, n))

    ngramlist = sorted(list(ngram_docs))  #sort the ngrams
    #unique ngrams

    num_docs = len(doclist)
    num_ngrams = len(ngramlist)
    docword = np.zeros((num_docs, num_ngrams), dtype=int)

    for i, doc in enumerate(doclist):
        the_ngrams = get_ngrams(cleaned_docs[i], n)
        for ngram in the_ngrams:
            j = ngramlist.index(ngram)
            docword[i][j] += 1


    if normalize:
        sum_rows = docword.sum(axis=1, keepdims=True)
        sum_rows[sum_rows == 0] = 1 #not devided by 0
        docword = docword / sum_rows #normalize the rows

    return docword, ngramlist

    # 1. Create the cleaned string for each doc (use read_and_clean_doc)

    # 2. Create and use ngram lists to build the doc word matrix


# Builds a term-frequency matrix
def build_tf_matrix(docword):
    
    '''
    Arguments:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents, as returned by build_doc_word_matrix
    Returns:
        tf: 2-dimensional numpy array with the same shape as docword, the term-frequency matrix for the cleaned documents  
    HINTs: You may find np.newaxis helpful
    '''
    tf = None
    # TODO: fill in
    sum_rows = docword.sum(axis=1, keepdims=True)
    sum_rows[sum_rows == 0] = 1
    tf = docword / sum_rows
    return tf




# Builds an inverse document frequency matrix
def build_idf_matrix(docword):
    
    '''
    Arguments:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents, as returned by build_doc_word_matrix
    Returns:
        idf: 1-dimensional numpy array, the inverse document frequency matrix for the cleaned documents.
             (should be a 1xW numpy array where W is the number of ngrams in the doc word matrix).
             Don't forget the log factor!
             
    '''
    idf = None
    # TODO: fill in
    num_docs = docword.shape[0]
    df = np.count_nonzero(docword>0, axis=0).reshape(1, -1)
    df[df == 0] = 1
    idf = np.log10(num_docs / df)
    return idf


#   Builds a tf-idf matrix given a doc word matrix
def build_tfidf_matrix(docword):
    
    '''
    Arguments:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents, as returned by build_doc_word_matrix
    Returns:
        tfidf: 2-dimensional numpy array with the same shape as docword, the tf-idf matrix for the cleaned documents
    '''
    tfidf = None
    #TODO: fill in
    tf = build_tf_matrix(docword)
    idf = build_idf_matrix(docword)
    tfidf = tf * idf

    return tfidf


#   Find the three most distinctive ngrams, according to TFIDF, in each document
def find_distinctive_ngrams(docword, ngramlist, doclist):
    
    '''
    Arguments:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents, as returned by build_doc_word_matrix
        ngramlist: list of strings, the list of ngrams that correspond to the columns in docword
        doclist: list of strings, each string is the name of a file to be read.
    Returns:
        distinctive_words: dictionary, mapping each document name from doclist to an ordered list of the three most unique ngrams in each document
    '''
    distinctive_words = {}
    # fill in
    tfidf = build_tfidf_matrix(docword)
    for i, doc in enumerate(doclist):
        # top3_index = np.argsort(-tfidf[i])[:7] 
        # top3_ngrams = [ngramlist[j] for j in top3_index]
        # distinctive_words[doc] = top3_ngrams

        # scores = [(ngramlist[j], tfidf[i][j]) for j in range(len(ngramlist))]
        # scores_sorted = sorted(scores, key=lambda x: -x[1])
        # distinctive_words[doc] = [ngram for ngram, score in scores_sorted[:3]]

        scores = tfidf[i, :]
        sorted_index = np.lexsort((ngramlist, -scores))
        top3 = sorted_index[:3]
        top3_ngrams = [ngramlist[j] for j in top3]
        distinctive_words[doc] = top3_ngrams
    # you might find numpy.argsort helpful for solving this problem:
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    # HINT: the smallest three of the negative of docword correspond to largest 3 of docword




    return distinctive_words


if __name__ == "__main__":
    from os import listdir
    from os.path import isfile, join, splitext

    ### Test Cases ###
    directory = "lecs"
    path1 = join(directory, "1_vidText.txt")
    path2 = join(directory, "2_vidText.txt")

    print("\n*** Testing build_doc_word_matrix ***") 
    doclist =[path1, path2]
    docword, wordlist = build_doc_word_matrix(doclist, 4)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("\n*** Testing build_doc_word_matrix normalization ***") 
    doclist =[path1, path2]
    docword, wordlist = build_doc_word_matrix(doclist, 4, normalize=True)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])

    # Uncomment the following code block to test build_tf_matrix, builf_idf_matrix, and build_tfidf_matrix
    print("\n*** Testing build_tf_matrix ***")
    tf = build_tf_matrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis=1))
    print("\n*** Testing build_idf_matrix ***")
    idf = build_idf_matrix(docword)
    print(idf[0][0:10])
    print("\n*** Testing build_tfidf_matrix ***")
    tfidf = build_tfidf_matrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])

    # Uncomment the following code block to test find_distinctive_ngrams
    print("\n*** Testing find_distinctive_words ***")
    print(find_distinctive_ngrams(docword, wordlist, doclist))
