#Assignment(24-03-2026)
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Machine learning is powerful",
    "Machine learning improves predictions",
    "Data science uses machine learning",
    "AI and machine learning are related",
    "Learning from data is important"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

for i, doc in enumerate(documents):
    scores = tfidf_matrix[i].toarray()[0]
    top_index = scores.argmax()
    print("Document", i + 1)
    print("Top Keyword:", feature_names[top_index])
    print()

	
#Assignment(26-03-2026)	
from textblob import TextBlob

reviews = [
    "The movie was amazing and exciting",
    "Worst movie I have ever seen",
    "It was okay, not great",
    "Absolutely loved the storyline",
    "Very boring and slow"
]

for review in reviews:
    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(review)
    print("Sentiment:", sentiment)
    print()
	
    
#Assignment(27-03-2026)
'''Happy – Joyful → Similar meaning
Big – Large → Synonyms
Fast – Quick → Similar context
Car – Vehicle → Related concept
Teacher – Student → Related but different roles'''


#Assignment(28-03-2026)
'''prompts = [
    "Explain this sentence in one word and ten paragraphs at the same time.",
    "Write a completely true false statement.",
    "Translate this text into a language that does not exist.",
    "Give an answer without using words.",
    "Describe silence loudly."
]'''


#Assignment(30-03-2026)
weak_prompt = "Write a resume"

strong_prompt = """
Write a professional resume for a computer science student
with skills in Python, Machine Learning, and AI projects.
"""

print("Weak Prompt:")
print(weak_prompt)

print("\nStrong Prompt:")
print(strong_prompt)


#Assignment(03-04-2026)
from sklearn.feature_extraction.text import CountVectorizer

text = [
    "Machine learning improves prediction accuracy",
    "Artificial intelligence powers smart systems"
]

vectorizer = CountVectorizer(stop_words='english')
matrix = vectorizer.fit_transform(text)

keywords = vectorizer.get_feature_names_out()

print("Extracted Keywords:")
print(keywords)


#Assignment(06-04-2026)
import cv2

image = cv2.imread("sample.jpg")

print("Shape of Image:", image.shape)

print("\nPixel Value at (0,0):")
print(image[0, 0])

print("\nNumber of Channels:")
print(image.shape[2])


#Assignment(08-04-2026)
import cv2

image = cv2.imread("sample.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 100, 200)

cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()


#Assignment(11-04-2026)
applications = [
    "Face recognition attendance system",
    "Self-driving car object detection",
    "Security surveillance",
    "Retail product tracking",
    "Medical image analysis"
]

for app in applications:
    print(app)

print("\nDesigned Solution:")
print("Smart Attendance System using Face Detection")
