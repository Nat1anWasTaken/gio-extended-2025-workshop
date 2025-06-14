# ADK 實驗專案

這是一個使用 Google Agent Development Kit (ADK) 建立的實驗專案，包含了基於 Gemini 模型的智能助手代理。

## 專案結構

```
adk-experiment/
├── default_adk_agent/     # 預設代理配置
│   ├── agent.py          # 代理定義
│   └── __init__.py
├── tool_adk_agent/       # 工具代理配置
├── main.py               # 主程式入口
├── pyproject.toml        # 專案配置
└── README.md            # 使用說明
```

## 系統需求

- Python 3.12 或更高版本
- Google Cloud 帳戶
- uv 套件管理器

## Google Cloud 憑證設定

### 1. 建立 Google Cloud 專案

1. 前往 [Google Cloud Console](https://console.cloud.google.com/)
2. 建立新專案或選擇現有專案
3. 記下您的專案 ID

### 2. 啟用必要的 API

在 Google Cloud Console 中啟用以下 API：

- Vertex AI API
- Cloud Resource Manager API

```bash
# 使用 gcloud CLI 啟用 API
gcloud services enable aiplatform.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
```

### 3. 設定服務帳戶

1. 在 Google Cloud Console 中，前往「IAM 與管理」>「服務帳戶」
2. 點擊「建立服務帳戶」
3. 輸入服務帳戶名稱和描述
4. 授予以下角色：
   - Vertex AI User
   - AI Platform Developer

### 4. 下載憑證金鑰

1. 在服務帳戶列表中，點擊您剛建立的服務帳戶
2. 前往「金鑰」標籤
3. 點擊「新增金鑰」>「建立新金鑰」
4. 選擇 JSON 格式並下載

### 5. 設定環境變數

在您的 shell 配置文件中（如 `~/.zshrc`）添加：

```bash
# Google Cloud 憑證設定
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
export GOOGLE_CLOUD_PROJECT="your-project-id"
```

重新載入 shell 配置：

```bash
source ~/.zshrc
```

### 6. 驗證憑證設定

```bash
# 安裝 gcloud CLI（如果尚未安裝）
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# 驗證憑證
gcloud auth application-default login
gcloud config set project your-project-id
```

## 安裝步驟

### 1. 複製專案

```bash
git clone <repository-url>
cd adk-experiment
```

### 2. 安裝 uv（如果尚未安裝）

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. 安裝依賴

```bash
uv sync
```

### 4. 啟動虛擬環境

```bash
source .venv/bin/activate
```

## 使用方法

### 啟動 ADK 開發伺服器

```bash
# 使用 uv 執行
uv run adk dev-ui

# 或在虛擬環境中執行
source .venv/bin/activate
adk dev-ui
```

### 訪問開發介面

伺服器啟動後，在瀏覽器中訪問：

- 本地測試：http://localhost:8000
- 開發介面：http://localhost:8000/dev-ui/?app=default_adk_agent

### 與代理互動

1. 在開發介面中選擇 `default_adk_agent`
2. 開始與 AI 助手對話
3. 代理會使用 Gemini 2.0 Flash Lite 模型回應您的問題

## 代理配置

### 預設代理 (default_adk_agent)

- **模型**：gemini-2.0-flash-lite
- **名稱**：root_agent
- **描述**：用於回答用戶問題的有用助手
- **指令**：盡力回答用戶問題

### 自定義代理

您可以修改 `default_adk_agent/agent.py` 來自定義代理行為：

```python
from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-2.0-flash-lite",
    name="your_agent_name",
    description="您的代理描述",
    instruction="您的自定義指令",
)
```

## 故障排除

### 常見問題

1. **憑證錯誤**

   - 確認 `GOOGLE_APPLICATION_CREDENTIALS` 環境變數指向正確的 JSON 金鑰文件
   - 確認服務帳戶具有必要的權限

2. **API 未啟用**

   - 確認已在 Google Cloud Console 中啟用 Vertex AI API

3. **專案 ID 錯誤**
   - 確認 `GOOGLE_CLOUD_PROJECT` 環境變數設定正確

### 檢查環境設定

```bash
# 檢查環境變數
echo $GOOGLE_APPLICATION_CREDENTIALS
echo $GOOGLE_CLOUD_PROJECT

# 測試 Google Cloud 連接
gcloud auth list
gcloud config list project
```

## 開發

### 添加新代理

1. 複製 `default_adk_agent` 目錄
2. 重新命名為您的代理名稱
3. 修改 `agent.py` 中的配置
4. 重新啟動開發伺服器

### 添加工具和功能

參考 Google ADK 文檔來添加更多功能：

- [Google ADK 官方文檔](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)

## 授權

此專案使用的授權條款請參考 LICENSE 文件。

## 貢獻

歡迎提交 Issue 和 Pull Request 來改進此專案。
