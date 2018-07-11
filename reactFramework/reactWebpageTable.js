//react table

//step 1. generate the data accortding to the table, using different mapping way
[
    {rate_period_months: 36, sale_month: "2003-01", expire_month: "2006-01", earned_month: 36, total_sales: 4253, …}
    {rate_period_months: 36, sale_month: "2003-02", expire_month: "2006-02", earned_month: 36, total_sales: 4495, …}
    {rate_period_months: 36, sale_month: "2003-03", expire_month: "2006-03", earned_month: 36, total_sales: 5411, …}
]

//step 2. generate all the header array using the same way: makeGenericHeader(col_list)
input:
["rate_period_months","sale_month","expire_month"]

output:
[
    {Header: "rate_period_months", accessor: "rate_period_months", filterable: true, Cell: ƒ}
    {Header: "sale_month", accessor: "sale_month", filterable: true, Cell: ƒ}
    {Header: "expire_month", accessor: "expire_month", filterable: true, Cell: ƒ}
]