from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.preprocess import clean_text

def get_match_score(resume, jd):
    resume = clean_text(resume)
    jd = clean_text(jd)

    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume, jd])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)

def get_missing_skills(resume, jd):
    resume_words = set(clean_text(resume).split())
    jd_words = set(clean_text(jd).split())

    return list(jd_words - resume_words)[:10]