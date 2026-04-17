from fastapi import FastAPI
from app.github import get_pr_diff
from app.reviewer import review_code

app = FastAPI()

@app.get("/review-pr")
def review_pr(owner, repo, pr):
    diff = get_pr_diff(owner, repo, pr)
    review = review_code(diff)

    return {
        "review": review
    }