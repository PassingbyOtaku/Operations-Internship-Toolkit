from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import difflib
from datetime import datetime
import os

# 初始化Flask应用
app = Flask(__name__)
CORS(app)  # 允许跨域请求，方便本地HTML调用

# 获取当前文件所在目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class TextComparator:
    @staticmethod
    def compare_texts(text1, text2):
        """比对两段文本并返回差异结果"""
        differ = difflib.Differ()
        return list(differ.compare(text1.splitlines(), text2.splitlines()))

    @staticmethod
    def generate_html_report(diff_result, file1_name, file2_name):
        """生成HTML格式的差异报告"""
        table_rows = []
        line_num1, line_num2 = 1, 1
        
        for line in diff_result:
            if line.startswith('  '):
                # 无变化的行
                table_rows.append(f'<tr class="diff-unchanged"><td>{line_num1}</td><td>{line[2:]}</td><td>{line_num2}</td><td>{line[2:]}</td></tr>')
                line_num1 += 1
                line_num2 += 1
            elif line.startswith('+ '):
                # 新增的行
                table_rows.append(f'<tr class="diff-added"><td></td><td></td><td>{line_num2}</td><td>{line[2:]}</td></tr>')
                line_num2 += 1
            elif line.startswith('- '):
                # 删除的行
                table_rows.append(f'<tr class="diff-removed"><td>{line_num1}</td><td>{line[2:]}</td><td></td><td></td></tr>')
                line_num1 += 1
            elif line.startswith('? '):
                # 差异标记行，暂时忽略
                continue

        return '<table class="diff-table"><tr><th>原始文件行号</th><th>原始内容</th><th>修改后行号</th><th>修改后内容</th></tr>' + ''.join(table_rows) + '</table>'

@app.route('/')
def serve_index():
    """提供HTML界面"""
    return send_from_directory(BASE_DIR, 'template.html')

@app.route('/status')
def check_status():
    """检查服务器状态"""
    return jsonify({'status': 'ok', 'message': '服务器运行正常'})

@app.route('/compare', methods=['POST'])
def compare_files():
    """处理文本比对请求"""
    try:
        data = request.json
        text1 = data.get('text1', '')
        text2 = data.get('text2', '')
        file1_name = data.get('file1Name', '未知文件1')
        file2_name = data.get('file2Name', '未知文件2')

        # 比对文本
        comparator = TextComparator()
        diff_result = comparator.compare_texts(text1, text2)
        diff_table = comparator.generate_html_report(diff_result, file1_name, file2_name)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return jsonify({
            'status': 'success',
            'timestamp': timestamp,
            'diffTable': diff_table,
            'file1Name': file1_name,
            'file2Name': file2_name
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'比对过程出错: {str(e)}'
        }), 500

if __name__ == '__main__':
    # 在本地8000端口启动服务器，自动打开浏览器
    print('文本差异比对工具服务器启动中...')
    print(f'请在浏览器中访问: http://localhost:8000')
    print('按Ctrl+C停止服务器')
    import webbrowser
    webbrowser.open('http://localhost:8000')
    app.run(host='0.0.0.0', port=8000, debug=False)