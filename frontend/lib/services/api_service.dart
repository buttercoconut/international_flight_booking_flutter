import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/flight.dart';

class ApiService {
  static const String _baseUrl = 'https://api.example.com';

  Future<List<Flight>> fetchFlights({
    required String origin,
    required String destination,
    required DateTime date,
    required int passengers,
  }) async {
    final uri = Uri.parse('$_baseUrl/flights').replace(queryParameters: {
      'origin': origin,
      'destination': destination,
      'date': date.toIso8601String(),
      'passengers': passengers.toString(),
    });

    final response = await http.get(uri);
    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body) as List<dynamic>;
      return data.map((e) => Flight.fromJson(e as Map<String, dynamic>)).toList();
    } else {
      throw Exception('Failed to load flights');
    }
  }
}
