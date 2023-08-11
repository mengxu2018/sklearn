from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 只选择Setosa和Versicolor两类
X = X[(y == 0) | (y == 1)]
y = y[(y == 0) | (y == 1)]

# 将数据集分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建SVM分类器并进行训练
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = clf.predict(X_test)

# 计算分类准确率
accuracy = accuracy_score(y_test, y_pred)
print("分类准确率:", accuracy)

# 创建新的花朵样本数据，进行分类预测
new_samples = [[5.1, 3.5, 1.4, 0.2], [6.0, 3.0, 4.8, 1.8]]
predictions = clf.predict(new_samples)
print("新样本的分类预测:", predictions)
