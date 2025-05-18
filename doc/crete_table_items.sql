-- items テーブル
CREATE TABLE public.items (
    id    SERIAL PRIMARY KEY,                     -- 自動採番 PK 兼インデックス
    name  VARCHAR(255)    NOT NULL,              -- 商品名
    price DOUBLE PRECISION NOT NULL,             -- 価格（Float 相当）
    tags  TEXT[]          DEFAULT ARRAY[]::TEXT[] -- 文字列配列。空配列をデフォルト
);