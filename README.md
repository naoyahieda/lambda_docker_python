# コード

# ローカルでのビルドとテスト

docker build -t myfunction:latest .
docker run -p 9000:8080 myfunction:latest

で起動してからの、ターミナルで curl するとローカルでテストできる(=Lambda の発火と同義)

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

# 参考:

https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/images-test.html
