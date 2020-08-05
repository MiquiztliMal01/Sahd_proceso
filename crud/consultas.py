import sqlite3

class query():
	def __init__(self):
		self.db = "database.db"
	def ejecutar_consultar(self,sql,parametros=()):
		with sqlite3.connect(self.db) as conn:
			cursor = conn.cursor()
			result = cursor.execute(sql,parametros)
			conn.commit()
			return result

	def save(self,nom,ap_p,ap_m,contra,huella,id_cargo,nip):
		sql = "INSERT INTO usuarios(nom,ap_p,ap_m,contra,huella,id_cargo,nip) VALUES(?,?,?,?,?,?,?)"
		parametros =(nom,ap_p,ap_m,contra,huella,id_cargo,nip)
		self.ejecutar_consultar(sql, parametros)

	def read(self):
		sql = "SELECT * FROM usuarios"
		results = self.ejecutar_consultar(sql)
		return results
		
	def delete(self,nom):
		sql = "DELETE FROM usuarios WHERE nom=?"
		parametros = (nom,)
		results = self.ejecutar_consultar(sql,parametros)

	def update(self,nip_nuevo,nom_nuevo,ap_p_nuevo,ap_m_nuevo,contra_nuevo,huella_nuevo,id_cargo_nuevo
				,nip,nom,ap_p,ap_m,contra,huella,id_cargo):
		sql = "UPDATE usuarios SET nip=?,nom=?,ap_p=?,ap_m=?,contra=?,huella=?,id_cargo=? WHERE nip=? AND nom=? AND ap_p=? AND ap_m=? AND contra=? AND huella=? AND id_cargo=?"
		parametros = (nip_nuevo,nom_nuevo,ap_p_nuevo,ap_m_nuevo,contra_nuevo,huella_nuevo,id_cargo_nuevo,nip,nom,ap_p,ap_m,contra,huella,id_cargo)
		self.ejecutar_consultar(sql,parametros)