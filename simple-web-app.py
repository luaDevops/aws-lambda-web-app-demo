from datetime import datetime

request_count = 0

def lambda_handler(event, context):
    global request_count
    request_count += 1

    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Mr. Paul L.| AWS Lambda Web App</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #020617, #1e293b);
                color: white;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .card {{
                background: rgba(30, 41, 59, 0.95);
                padding: 35px 50px;
                border-radius: 15px;
                box-shadow: 0px 15px 40px rgba(0,0,0,0.5);
                text-align: center;
                width: 380px;
            }}

            h1 {{
                margin-bottom: 10px;
            }}

            .badge {{
                display: inline-block;
                background: #16a34a;
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 13px;
                margin-bottom: 15px;
            }}

            .info {{
                margin-top: 15px;
                font-size: 14px;
                color: #cbd5e1;
            }}

            footer {{
                margin-top: 20px;
                font-size: 12px;
                color: #94a3b8;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">Server Status: Online</div>
            <h1>🚀 AWS Lambda Web App</h1>

            <div class="info">
                <p><strong>Developer:</strong> Mr. Paul Lulami Wamenya</p>
                <p><strong>Server Time:</strong> {current_time}</p>
                <p><strong>Request Count:</strong> {request_count}</p>
            </div>

            <footer>
                Serverless Architecture Demo<br>
                Powered by AWS Lambda
            </footer>
        </div>
    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html; charset=UTF-8"
        },
        "body": html_content
    }
