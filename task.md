# MongoDB Vector Search Assignment: Academic Paper Recommender

## Project Overview
Develop a research paper recommendation system using MongoDB Atlas Vector Search that helps researchers discover relevant academic papers based on semantic similarity.

## Technical Requirements
- Programming Language: Python
- Database: MongoDB Atlas
- Additional Libraries: 
  * `pymongo`
  * `sentence-transformers`
  * `numpy`

## Assignment Tasks

### 1. Data Preparation
- Collect a dataset of academic papers (minimum 500 papers)
- Sources can include:
  * ArXiv API
  * Kaggle datasets
  * Public research paper repositories

#### Data Fields
```python
paper_document = {
    "title": str,
    "abstract": str,
    "authors": list,
    "publication_year": int,
    "vector_embedding": list,  # Generated embedding
    "keywords": list,
    "doi": str
}
```

### 2. Embedding Generation
Create a script to:
- Generate vector embeddings for paper abstracts
- Use `sentence-transformers/all-MiniLM-L6-v2` model
- Embed abstracts into 384-dimensional vectors

### 3. MongoDB Atlas Vector Search Setup
- Create a MongoDB Atlas cluster
- Design a vector index for semantic search
- Implement insertion of papers with embeddings

### 4. Recommendation Engine
Develop a function `find_similar_papers(query_embedding, top_k=5)` that:
- Performs vector similarity search
- Ranks papers by semantic closeness
- Filters results by optional criteria (publication year, keywords)

### 5. Interactive CLI Application
Build a command-line interface that allows:
- Searching papers by abstract or keywords
- Displaying recommended papers
- Showing similarity scores

### 6. Performance Analysis
Create a report analyzing:
- Indexing time
- Search query response time
- Memory usage
- Accuracy of recommendations

## Evaluation Criteria
- Code quality and documentation
- Effective use of vector embeddings
- Performance optimization
- Creative approach to recommendation logic

## Bonus Challenges
- Implement caching mechanism
- Add machine learning model to improve recommendations
- Create visualization of paper relationships

## Submission Requirements
1. Complete Python project
2. README with setup instructions
3. Performance analysis report
4. Presentation slides explaining your approach
```

## Recommended Project Structure
paper_recommender/
│
├── data/
│   └── papers.json
│
├── src/
│   ├── embeddings.py
│   ├── database.py
│   └── recommender.py
│
├── requirements.txt
└── README.md
