class ApiSettings {
  // APIのベースURL（コンテナ）
  static const String baseUrl = 'http://localhost:8001';

  // APIのベースURL（ローカル）
  // static const String baseUrl = 'http://127.0.0.1:8000';

  // エンドポイント
  static const String usersEndpoint = '$baseUrl/users';
}
