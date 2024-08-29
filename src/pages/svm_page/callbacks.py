from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from dash import Input, Output, callback
from src.pages.svm_page.figures import *
from sklearn.svm import SVC
import numpy as np
import logging

logger = logging.getLogger("MyNewApp") # make sure to change the name in logging.conf
@callback(
    Output("svm-degree", "disabled"),
    [Input("svm-kernel", "value")],
    prevent_initial_call=True,
)
def disable_slider_param_degree(kernel):
    return kernel != "poly"

@callback(
    Output("svm-gamma", "disabled"),
    [Input("svm-kernel", "value")],
    prevent_initial_call=True,

)
def disable_slider_param_gamma_coef(kernel):
    return kernel not in ["rbf", "poly", "sigmoid"]

@callback(
        Output("svm-plot", "figure"),
        Output("svm-roc", "figure"),
        Output("svm-cm", "figure"),
    [
        Input("svm-kernel", "value"),
        Input("svm-degree", "value"),
        Input("svm-c", "value"),
        Input("svm-gamma", "value"),
        Input("svm-dataset", "value"),
        Input("svm-noise", "value"),
        Input("svm-n-samples", "value"),
    ],
)
def update_svm_graph(
    kernel,
    degree,
    C_coef,
    gamma_coef,
    dataset,
    noise,
    sample_size,
):
    
    h = 0.3  # step size in the mesh

    # Data Pre-processing
    X, y = generate_data(n_samples=sample_size, dataset=dataset, noise=noise)
    X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )

    x_min = X[:, 0].min() - 0.5
    x_max = X[:, 0].max() + 0.5
    y_min = X[:, 1].min() - 0.5
    y_max = X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    # Train SVM
    clf = SVC(C=C_coef, kernel=kernel, degree=degree, gamma=gamma_coef)
    clf.fit(X_train, y_train)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

    prediction_figure = serve_prediction_plot(
        model=clf,
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        Z=Z,
        xx=xx,
        yy=yy,
        mesh_step=h,
    )

    roc_figure = serve_roc_curve(model=clf, X_test=X_test, y_test=y_test)

    confusion_figure = serve_pie_confusion_matrix(
        model=clf, X_test=X_test, y_test=y_test, Z=Z
    )
    logger.info(f"Updated updated with kernel={kernel}, degree={degree}, C={C_coef}, gamma={gamma_coef}, dataset={dataset}, noise={noise}, sample_size={sample_size}")
    return [prediction_figure, roc_figure, confusion_figure]

def generate_data(n_samples, dataset, noise):
    if dataset == "moons":
        return make_moons(n_samples=n_samples, noise=noise, random_state=0)

    elif dataset == "circles":
        return make_circles(
            n_samples=n_samples, noise=noise, factor=0.5, random_state=1
        )

    elif dataset == "linear":
        X, y = make_classification(
            n_samples=n_samples,
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=2,
            n_clusters_per_class=1,
        )

        rng = np.random.RandomState(2)
        X += noise * rng.uniform(size=X.shape)
        linearly_separable = (X, y)

        return linearly_separable

    else:
        raise ValueError(
            "Data type incorrectly specified. Please choose an existing dataset."
        )
