import pandas as pd
import numpy as np
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import operator
import re

anime = pd.read_excel('animeinfo.xlsx', sheet_name='애니메이션')
product = pd.read_excel('animeinfo.xlsx', sheet_name='식품')
product_infor = pd.read_excel('animeinfo.xlsx', sheet_name='단어들')
# print(anime)
# print(product)
# print(product_infor)
# print(product['식품'].tolist(),product_infor['형용사'][:6].tolist(), product_infor['나이'][:5].tolist())

def getProductFood():
    return product['식품'].tolist()

def getProductFoodInfo():
    return product_infor['형용사'][:18].tolist()

def getProductFoodInfo2():
    return product_infor['명사'][:45].tolist()

def getAge():
    return product_infor['나이'][:4].tolist()

anime = anime[['이름', '소개글', '테마']]
# print(anime_matrix)
anime.loc[:, '소개글'] = anime['소개글'].apply(lambda x: re.sub('[^\w\s]', '', x))
# print(anime['소개글'])
# anime.loc[:, '테마'] = anime['테마'].apply(lambda x: ' '.join(x))
# print(anime['테마'])
anime_matrix = anime['소개글'] + ' ' + anime['테마']
# print(anime_matrix.shape)
# print(anime_matrix)

twitter = Okt()
def tw_tokenizer(text):
    tokens_ko = twitter.morphs(text)
    return tokens_ko

def similar_animes(product_info, matrix=anime_matrix, k=5):
    tfidf_vect = TfidfVectorizer(tokenizer=tw_tokenizer, ngram_range=(1, 2), min_df=3, max_df=0.9)
    feature_vect = tfidf_vect.fit_transform(matrix)
    # print(feature_vect.shape)
    # feature_names = tfidf_vect.get_feature_names_out()
    # print(feature_names)

    # pos_tags = twitter.pos(' '.join(feature_names))
    # adjectives_list = [word for word, pos in pos_tags if pos == 'Adjective']
    # nouns_list = [word for word, pos in pos_tags if pos == 'Noun']
    # np.savetxt('data.txt', adjectives_list, fmt='%s', encoding='utf-8')
    # np.savetxt('data1.txt', nouns_list, fmt='%s', encoding='utf-8')

    # feature_vect_dense = feature_vect.todense()
    # print(feature_vect_dense)

    product_tfidf = tfidf_vect.transform(product_info)

    similarities = cosine_similarity(product_tfidf, feature_vect).flatten()

    anime_list = matrix.index.tolist()

    anime_similarity = dict(zip(anime_list, similarities))
    anime_similarity_sorted = sorted(anime_similarity.items(), key=operator.itemgetter(1), reverse=True)

    top_anime_similarities = anime_similarity_sorted[:k]
    animes = [anime.iloc[i[0]]['이름'] for i in top_anime_similarities]

    return animes

def recommend_anime(product_index, similar_anime_indices, matrix=product, k=3):
    columns = matrix.columns.isin(similar_anime_indices)
    similar_anime = matrix.iloc[:, columns]
    # print(similar_anime)

    product_list = matrix['식품'].tolist()
    # print(product_list)

    index = product_list.index(product_index)
    # print(index)

    product_anime = similar_anime.iloc[index, :]
    # print(type(product_anime))
    # print(product_anime)

    sorted_product_anime = product_anime.sort_values(ascending=False)
    # print(sorted_product_anime)

    top_sorted_product_anime = sorted_product_anime[:k]
    recommendAnime = top_sorted_product_anime.index.tolist()

    # print(similar_anime_indices[0])
    if similar_anime_indices[0] in recommendAnime:
        return recommendAnime
    else:
        recommendAnime[k - 1] = similar_anime_indices[0]
        return recommendAnime

# product_index = '빵'
# product_info = '뽀로로와 노래해요 라라라라라라'
# #
# animes = similar_animes(product_info=product_info, matrix=anime_matrix, k=5)
# print(animes)
# recommend = recommend_anime(product_index=product_index, similar_anime_indices=animes, matrix=product, k=3)
# print(recommend)