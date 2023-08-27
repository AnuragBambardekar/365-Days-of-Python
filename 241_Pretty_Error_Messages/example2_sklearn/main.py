import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

import pretty_errors

pretty_errors.configure(
    separator_character='*',
    filename_display=pretty_errors.FILENAME_EXTENDED,
    line_color=pretty_errors.RED + '> ' + pretty_errors.default_config.line_color,
    lines_before=5,
    lines_after=5
)

X,y = make_classification(n_samples=1000, n_features=20, random_state=42)

def create_pipeline():
    steps = [
        ('standard_scaler', StandardScaler()),
        ('pca',PCA(n_components=15)),
        ('classifier',RandomForestClassifier())
    ]
    pipeline = Pipeline(steps)
    return pipeline

if __name__ == "__main__":
    p = create_pipeline()
    X_bad = X[:, 10] # first 10 features
    
    # will cause a problem because PCA has 15 components, but we are passing 10 features
    p.fit(X_bad) 