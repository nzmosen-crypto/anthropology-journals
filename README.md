# 文化人類學期刊 · 最新一期 / Cultural Anthropology Journals — Latest Issues

每月自動抓取 28 本文化人類學期刊的最新一期目錄與摘要，發佈成公開網頁與 RSS。
Every month this repository collects the latest-issue tables of contents (with abstracts) of 28 cultural anthropology journals and publishes them as a web page and an RSS feed.

## 訂閱 / Subscribe

- **網頁 / Web page**：本 repo 的 GitHub Pages（Settings → Pages 顯示網址）
- **RSS**：網頁網址後加 `feed.xml`。加到 Feedly、Inoreader 等閱讀器，任一期刊出新一期就會收到一則。
- **Email**：把 RSS 網址貼到 Blogtrottr、Feedrabbit 等免費 RSS-to-email 服務。

## 期刊 / Journals (`journals.csv`)

選刊條件：SCImago (SJR) 人類學類 Q1；沒有 Q1 時，選該領域公認具高度學術聲望的期刊；皆為同儕審查（peer-reviewed）期刊。`review` 欄另註明是否已確認為雙盲。
Selection: SJR Q1 in Anthropology where possible, otherwise highly prestigious in the field; all peer-reviewed. The `review` column notes whether double-blind review was confirmed.

每本期刊的 SJR 分級與審查方式記在 `journals.csv` 的 `sjr_note`、`review` 欄（2026 年 11 月查核）。

- 22 English · 3 日本語（CiNii Research）· 3 한국어（KCI 등재지；Crossref）
- 「Double-blind (verified)」＝出版社或期刊網站明文寫雙盲；其餘為同儕審查、但雙盲與否未能從官方頁面確認（*Current Anthropology*、*JRAI* 及日、韓期刊）。

## 資料來源 / Data sources

Crossref、CiNii Research、OpenAlex（補摘要）。部分出版社登記期別較慢，新文章會列在「Online first」。

## 修改 / Editing

- 增刪期刊：編輯 `journals.csv`，存檔後會自動重跑。
- 手動執行：Actions → *Update anthropology journals* → Run workflow。
- 寄信給自己（選用）：在 Settings → Secrets → Actions 加 `GMAIL_USER`、`GMAIL_APP_PASSWORD`、`MAIL_TO`。
