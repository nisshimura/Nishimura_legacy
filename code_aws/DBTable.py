#!/usr/bin/env python
# coding: utf-8
#

"""
Database Table定義モジュール
"""

from pathlib import Path
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import make_transient

Base = declarative_base()

DB_PROTOCOL = 'sqlite:///'
DB_DIR = 'database/'
DB_FILENAME = 'veterans.db'
DB_DEFAULT_PATH = DB_DIR + DB_FILENAME

class DBEngine:
  """
  データベース(sqlalchemy Object Relational Mapping)エンジンクラス(Singleton)
  """

  _engine = None
  _db_url = DB_PROTOCOL + DB_DEFAULT_PATH

  def __new__(cls, *args, **kargs):
    """
    newコンストラクタ
    """
    if not hasattr(cls, "_instance"):
      cls._instance = super(DBEngine, cls).__new__(cls)
    return cls._instance

  def __init__(self):
    """
    コンストラクタ
    """
    return

  def getEngine(self):
    """
    Database Engine Instance の取得

    Returns:
        Database　Engine Instance
    """
    if not self._engine:
      self._engine = create_engine(DB_URL, echo=False)
      Base.metadata.create_all(self._engine)
    return self._engine

  def createEngine(self, url=None, dir=None):
    """
    Database Engine Instance の生成

    Args:
      url: データベースファイルのファイル名付きの保存先のパス指定：未指定の場合は、引数 dir にてデータベースファイルを作成
      dir: データベースファイルの保存先ディレクトリ指定のパス指定：未指定の場合は、デフォルト値のパス、ファイル名でデータベースファイルを生成

    Returns:
      Database　Engine Instance
    """
    self._db_url = self.getDBPath(url, dir)
    self._engine = create_engine(self._db_url, echo=False)
    Base.metadata.create_all(self._engine)
    return self._engine

  def getDBPath(self, url=None, dir=None):
    """
    Database ファイルの保存先パスの生成

    Args:
      url: データベースファイルのファイル名付きの保存先のパスの生成：未指定の場合は、引数 dir にてデータベースファイルを作成
      dir: データベースファイルの保存先ディレクトリ指定のパスの生成：未指定の場合は、デフォルト値のパス、ファイル名でデータベースファイルを生成

    Returns:
      Databaseファイルパス
    """
    if url:
      return url
    if dir:
      dir_path = Path(dir)
      dir_path.mkdir(parents=True, exist_ok=True)
      db_path = dir_path.joinpath(DB_FILENAME).absolute()
      return DB_PROTOCOL + str(db_path)

    return DB_PROTOCOL + DB_DEFAULT_PATH


class Note(Base):
  """
  KノートのDatabase Table定義
  """
  __tablename__ = 'mynotes'
  nid = Column(Integer, primary_key=True)
  country = Column(String)
  model = Column(String)
  eng_type = Column(String)
  pfp = Column(String)
  title = Column(String)
  cs = Column(String)
  dtc = Column(String)
  link = Column(String)
  cm = Column(String)
  cm_date = Column(String)
  memo = Column(String)
  etc1 = Column(String)
  etc2 = Column(String)
  etc3 = Column(String)
  status = Column(String)
  level = Column(Integer)
  search_target = Column(Integer)

  def __init__(self,
               nid=None,
               country="",
               model="",
               eng_type="",
               pfp="",
               title="",
               cs="",
               dtc="",
               link="",
               cm="",
               cm_date="",
               memo="",
               etc1="",
               etc2="",
               etc3="",
               status="",
               level=0,
               search_target=1):
    self.nid = nid
    self.country = country
    self.model = model
    self.eng_type = eng_type
    self.pfp = pfp
    self.title = title
    self.cs = cs
    self.dtc = dtc
    self.link = link
    self.cm = cm
    self.cm_date = cm_date
    self.memo = memo
    self.etc1 = etc1
    self.etc2 = etc2
    self.etc3 = etc3
    self.level = level
    self.status = status
    self.search_target = search_target
