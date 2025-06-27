import 'dart:convert';
import 'package:frontend/models/user.dart';
import 'package:http/http.dart' as http;
import 'api_settings.dart';

class UserService {
  Future<List<User>> fetchUsers() async {
    final response = await http.get(Uri.parse(ApiSettings.usersEndpoint));
    if (response.statusCode == 200) {
      final body = utf8.decode(response.bodyBytes);
      final List<dynamic> jsonList = json.decode(body);
      return jsonList.map((json) => User.fromJson(json)).toList();
    } else {
      throw Exception('ユーザー一覧の取得に失敗しました');
    }
  }
}
