from ase.db import connect

db_fn = "test.db"
db = connect(db_fn)

total_num = db.count()
print(f"total_num: {total_num}")

cal_num = db.count("vasp_calc=Yes")
print(f"cal_num: {cal_num}")

row_specific = db.get(id=1)
print(row_specific)
key_value_pairs = row_specific.key_value_pairs
print(f"key_value_pairs: {key_value_pairs}")

atoms_specific = db.get_atoms(id=1)
print(atoms_specific)


# for row in db.select("id<=10"):
for row in db.select("epa<-4.5"):
    print(row.epa)


db_output_fn = "test_output.db"
db_output = connect(db_output_fn)
for row in db.select("vasp_calc=Yes"):
    key_value_pairs = row.key_value_pairs
    data = row.data
    atoms = row.toatoms()
    db_output.write(atoms=atoms, key_value_pairs=key_value_pairs, data=data)
