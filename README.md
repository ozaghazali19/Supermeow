## 🌟 Features

| Feature       | Status  | Description                       |
| ------------- | ------- | --------------------------------- |
| Auto Check-in | On/Off  | Check-in daily to get more points |
| Auto Do Task  | On/Off  | Complete tasks                    |
| Auto Claim    | Dafault | Claim points when available       |

## 🚀 Run File

| Run with Proxy                   | Run without Proxy   |
| -------------------------------- | ------------------- |
| `bot-proxy.py` `data-proxy.json` | `bot.py` `data.txt` |

## ⚠️ Note

- Get auth data in the `Network` tab in DevTools.
  - `Network` --> Filter `info` or `balances` --> `Payload` --> `auth_data`
  - Starts with `%7B%22query_id%22...`
- Auto features: Change `false` to `true` in the `config.json` file.