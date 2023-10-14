# プロバイダの設定
provider "google" {
  credentials = file("path/to/your/credentials.json")  # サービスアカウントキーのパス
  project    = "your-project-id"  # GCPプロジェクトのID
  region     = "us-central1"  # リージョンを選択
}

# GCSバケットの設定
resource "google_storage_bucket" "terraform_backup" {
  name          = "your-unique-bucket-name"  # バケット名（一意である必要があります）
  location      = "US"  # バケットのリージョン
  force_destroy = true  # バケットの強制削除を許可

  versioning {
    enabled = true  # バージョニングを有効にする
  }

  lifecycle_rule {
    condition {
      age = 7  # バックアップを保存する日数（ここでは7日）
    }
    action {
      type = "SetStorageClass"
      storage_class = "STANDARD"  # ストレージクラスを指定
    }
  }

  uniform_bucket_level_access = true  # ユニフォームバケットレベルのアクセスを有効にする
}

# ローカルのTerraformコードをGCSバケットにアップロード
resource "google_storage_bucket_object" "terraform_code_backup" {
  name   = "backup/terraform.tf"  # アップロード先のオブジェクト名
  bucket = google_storage_bucket.terraform_backup.name
  source = "path/to/your/terraform/code"  # ローカルのTerraformコードのパス
}

# インターネットからのアクセスを制限
resource "google_storage_default_object_access_control" "terraform_backup_acl" {
  bucket = google_storage_bucket.terraform_backup.name
  entity = "allUsers"
  role   = "READER"
}
