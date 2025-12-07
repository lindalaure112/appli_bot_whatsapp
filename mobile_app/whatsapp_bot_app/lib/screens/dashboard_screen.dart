import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:whatsapp_bot_app/provider/auth_provider.dart';
import 'package:whatsapp_bot_app/screens/auth/login_screen.dart';

class DashboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final authProvider = Provider.of<AuthProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('Tableau de bord'),
        actions: [
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: () async {
              await authProvider.logout();
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(builder: (context) => LoginScreen()),
              );
            },
          ),
        ],
      ),
      body: Center(child: Text('Bienvenue dans le tableau de bord!')),
    );
  }
}
