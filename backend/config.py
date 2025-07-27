import os


class Config:
    """Classe base para configurações gerais da aplicação."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa o rastreamento de modificações
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # URI do banco de dados

class DevelopmentConfig(Config):
    """Configurações específicas para desenvolvimento"""
    DEBUG = True

class TestingConfig(Config):
    """Configurações específicas para testes"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///meubanco_test.db'  # Banco de dados de teste

class ProductionConfig(Config):
    """Configurações específicas para produção"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # URL do banco de dados em produção
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_para_producao'
