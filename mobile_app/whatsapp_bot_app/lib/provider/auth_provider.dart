import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:whatsapp_bot_app/services/api_service.dart';

class AuthProvider extends ChangeNotifier {
  bool _isLoading = false;
  bool _isLoggedIn = false;
  String? _token;
  String? _errorMessage;

  bool get isLoading => _isLoading;
  bool get isLoggedIn => _isLoggedIn;
  String? get token => _token;
  String? get errorMessage => _errorMessage;

  Future<void> login(String username, String password) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      final response = await ApiService.login(username, password);
      if (response['success'] == true && response['token'] != null) {
        _token = response['token'];
        _isLoggedIn = true;

        final prefs = await SharedPreferences.getInstance();
        await prefs.setString('token', _token!);
      } else {
        _errorMessage = response['message'] ?? 'Erreur inconnue';
        _isLoggedIn = false;
      }
    } catch (e) {
      _errorMessage = 'Erreur réseau ou serveur';
      _isLoggedIn = false;
    }

    _isLoading = false;
    notifyListeners();
  }

  Future<void> logout() async {
    _token = null;
    _isLoggedIn = false;
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('token');
    notifyListeners();
  }

  Future<void> checkLoginStatus() async {
    final prefs = await SharedPreferences.getInstance();
    _token = prefs.getString('token');
    _isLoggedIn = _token != null;
    notifyListeners();
  }
}
