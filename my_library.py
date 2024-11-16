def test_load():
  return 'loaded'

def compute_probs(x, y):
  p0 = x/(x+y)
  p1 = y/(x+y)
  return [p0,p1]

def cond_prob(table, column, column_value, target_column, target_column_value):
  assert column in table
  assert target_column in table
  assert column_value in up_get_column(table, column)

def cond_probs_product(full_table, evidence_row, target_column, target_column_value):
  assert target_column in full_table
  assert target_column_value in up_get_column(full_table, target_column)
  assert isinstance(evidence_row, list)
  assert len(evidence_row) == len(up_list_column_names(full_table)) - 1

def prior_prob(full_table, the_column, the_column_value):
  assert the_column in full_table
  assert the_column_value in up_get_column(full_table, the_column)


def naive_bayes(full_table, evidence_row, target_column):
  assert target_column in full_table
  assert isinstance(evidence_row, list)
  assert len(evidence_row) == len(up_list_column_names(full_table)) - 1
