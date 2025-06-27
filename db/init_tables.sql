-- CREATE TABLE users (
--   id SERIAL PRIMARY KEY,
--   name TEXT NOT NULL,
--   email TEXT UNIQUE NOT NULL
-- );

-- users（参加者情報）
CREATE TABLE users (
    id INTEGER PRIMARY KEY,         -- ユーザーID
    employee_code VARCHAR(255),     -- 社員番号
    nickname VARCHAR(255),          -- ニックネーム
    admin BOOLEAN                   -- 管理者か否か
);

-- teams（チーム情報）
CREATE TABLE teams (
    id INTEGER PRIMARY KEY,         -- チームID
    team_name VARCHAR(255)          -- チーム名（A, B, Cなど）
);

-- missions（ミッション内容）
CREATE TABLE missions (
    id INTEGER PRIMARY KEY,         -- ミッションID
    title VARCHAR(255),             -- タイトル（短文）
    description TEXT,               -- 詳細説明
    point_value INTEGER,            -- 獲得ポイント
    flag BOOLEAN                    -- 達成すべきかのフラグ
);

-- user_missions（ミッション進捗）
CREATE TABLE user_missions (
    id INTEGER PRIMARY KEY,         -- レコードID
    user_id INTEGER,                -- 参加者ID
    mission_id INTEGER,             -- ミッションID
    status VARCHAR(255),            -- 状態（未着手/実行中/完了など）
    points INTEGER,                 -- 獲得済ポイント数
    completed_at TIMESTAMP,         -- 達成日時
    proof_image_url TEXT,           -- 証拠画像の保存URL（任意）
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (mission_id) REFERENCES missions(id)
);

-- ユーザーとチームの紐付け（多対多の場合は中間テーブルを作成）
CREATE TABLE user_teams (
    user_id INTEGER,
    team_id INTEGER,
    PRIMARY KEY (user_id, team_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);
