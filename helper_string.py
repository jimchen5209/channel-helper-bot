#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Channel Helper Bot """
""" helper_string.py """
""" Copyright 2018, Jogle Lew """

import helper_global

helper_string = {
    "development_text": "該功能正在開發中...",
    "permission_denied_text": "權限不足",
    "reload_cmd_success": "重新載入完成！",
    "reload_cmd_failed": "嗯，好像出現了一些問題呢…",
    "start_cmd_text": "這是由 JogleLew 開發的頻道回覆助手 Bot 。你可以使用 /help 命令查看詳細使用說明。", 
    "help_cmd_text": "歡迎使用 Channel Helper Bot，本 bot 可以為您的頻道提供回覆和展示評論信息的入口，從而為頻道提供互動的平臺。\nGithub鏈接：https://github.com/JogleLew/channel-helper-bot\n使用此 bot 即為允許本 bot 在您的頻道內進行發送、編輯和刪除操作，並收集和存儲評論信息。\n使用步驟：\n1. 使用 /register 命令登記您的頻道信息。\n2. 將此 bot 添加為頻道管理員。\n3. 完成。如需更改配置請使用 /option 命令。",
    "add_comment": "新增留言",
    "show_all_comments": "顯示所有留言",
    "comment_header": "===== 留言區 =====",
    "comment_empty": "",
    "start_comment_mode": "您已進入留言模式，向我發送消息即可進行留言。使用 /cancel 命令可以中止留言模式。",
    "stop_comment_mode": "您已退出留言模式",
    "comment_success": "留言成功",
    "comment_edit_success": "編輯留言成功",
    "prev_page": "上一頁",
    "next_page": "下一頁",
    "no_prev_page": "沒有上一頁了",
    "no_next_page": "沒有下一頁了",
    "register_cmd_text": "請先將本 bot 添加為頻道的管理員（注：只需要在頻道設置中添加管理員，搜索本 bot 的 username，點擊添加即可），並授予 bot 發送、編輯、刪除消息的權限。然後從您的頻道中轉發一條消息（這條消息不能是轉發的別處的消息）給我，以便我獲取頻道的 ID。",
    "register_cmd_invalid": "這條消息中似乎不包含頻道信息呢...請從您的頻道中轉發一條消息給我",
    "register_cmd_not_admin": "您看起來不是頻道的管理員呢，本 bot 無法為您進行登記",
    "register_cmd_no_permission": "檢測到您沒有給本 bot 提供發送、編輯、刪除消息的權限。修改完權限後，請重新執行登記操作。",
    "register_cmd_no_info": "本 bot 無法獲取您的頻道信息，請檢查是否已經將本 bot 添加為頻道管理員。",
    "register_cmd_failed": "您的頻道信息可能已被記錄，如有問題請聯繫管理員",
    "register_cmd_success": "您的頻道信息已成功記錄，並啟用了默認的留言設置。如需修改設置，請使用 /option 命令。",
    "register_delete_info": "感謝您使用本 bot ！檢測您已經將本 bot 移出您的頻道，我們已刪除您的頻道登記信息。如需繼續使用請重新執行 /register 登記操作。",
    "option_no_channel": "您還沒有登記過頻道信息，請先使用 /register 命令完成登記。",
    "option_delete": "刪除頻道記錄",
    "option_record_deleted": "頻道記錄已刪除，感謝您的使用！",
    "option_finish": "完成設置",
    "option_finished": "設置已完成",
    "option_choose_channel": "請選擇一個頻道以進行設置",
    "option_choose_item": "請選擇一個項目以進行設置\nmode: bot 的工作模式\nrecent: 在頻道中顯示的留言數量",
    "option_choose_mode_value": "本 bot 有三種工作模式\n模式 0: 手動模式。當頻道中新增消息時，bot 不會自動創建留言消息。當頻道管理員使用 /comment 回覆需要評論的原始消息時，bot 才會創建評論消息。如果 /comment 命令不起作用，請檢查是否授予 bot 刪除消息的權限。\n模式 1: 自動模式。當頻道中新增消息時，bot 自動創建評論消息。該模式能保持原始頻道消息不被修改。\n模式 2: 自動模式(beta)。當頻道中新增消息時，bot 會嘗試編輯原消息，顯示添加評論按鈕。如果編輯失敗則直接創建評論消息。該模式能儘可能減少頻道里的評論區數量。\n請選擇您所需要的工作模式：",
    "option_choose_recent_value": "在頻道中僅顯示最近的若干條消息。請選擇頻道顯示的最近條目數量：",
    "option_update_success": "設置更新成功",
    "option_update_failed": "設置更新失敗",
    "clean_cmd_start": "正在進行檢查，請稍候...",
    "clean_cmd_deleted": "刪除記錄成功",
    "clean_cmd_set": "設置成功",
    "fwd_source": "消息來源: "
}

for item, value in helper_string.items():
    helper_global.assign(item, value)
