import 'package:flutter/material.dart';
import 'package:frontend/pages/register_page.dart';
import 'package:frontend/pages/user_list_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      // home: const MyHomePage(),
      initialRoute: '/register',
      routes: {
        '/register': (context) => const RegisterPage(),
        '/users': (context) => const UserListPage(),
      },
    );
  }
}
