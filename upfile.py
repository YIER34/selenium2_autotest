# 上传文件：
# 普通上传--将本地文件路径作为一个值放在input标签，通过form表单提交到服务器
# 插件上传--基于Flash、JavaScript、Ajax等技术实现的上传功能

# 1. send_keys实现上传
# 定位上传按钮，添加本地文件
driver.find_element_by_id("xxx").send_keys("file_path")

# 2. autolt实现上传（不推荐）