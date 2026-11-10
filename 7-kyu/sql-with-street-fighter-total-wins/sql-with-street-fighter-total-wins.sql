SELECT 
  f.name,
  SUM(f.won) AS won,
  SUM(f.lost) AS lost
FROM 
  fighters f
JOIN 
  winning_moves w ON f.move_id = w.id
WHERE 
  w.move NOT IN ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY 
  f.name
ORDER BY 
  won DESC
LIMIT 6;