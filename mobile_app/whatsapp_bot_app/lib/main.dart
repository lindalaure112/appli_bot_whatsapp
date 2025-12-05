import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:whatsapp_bot_app/provider/auth_provider.dart';
import 'package:whatsapp_bot_app/screens/dashboard_screen.dart';
import 'package:whatsapp_bot_app/screens/auth/login_screen.dart';

void main() async {
  await dotenv.load(fileName: ".env");
  runApp(
    MultiProvider(
      providers: [ChangeNotifierProvider(create: (_) => AuthProvider())],
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: Provider.of<AuthProvider>(
        context,
        listen: false,
      ).checkLoginStatus(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return MaterialApp(
            home: Scaffold(body: Center(child: CircularProgressIndicator())),
          );
        } else {
          final authProvider = Provider.of<AuthProvider>(context);
          return MaterialApp(
            title: 'WhatsApp Bot',
            theme: ThemeData(primarySwatch: Colors.blue),
            home: authProvider.isLoggedIn ? DashboardScreen() : LoginScreen(),
          );
        }
      },
    );
  }
}
