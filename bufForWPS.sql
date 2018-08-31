def plot_result(train, predicted, name, test=np.array([])):
    # print("predicted: ", predicted)
    # print("test: ", test)
    plt.figure(figsize=(16, 8))
    plt.title(name)  -- to show figure title
    plt.plot(train, label='Train')
    plt.plot(predicted, marker='o', label='Predicted')
    if int(len(test)) > 0:
        plt.plot(test, marker='o', label='Test')
    plt.legend()  --to show labels
    plt.show()

def load_positive_cover_demo(database, cover_file, batch_size):
    """
    Load demo data for provisioned covers
    """
    col_num = 1

    # batch_size = 300
    table_name = "table_example"
    cols = (
        "col1",
        "col2",
        ...
        "col3",
    )

    with open(cover_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        title = next(reader)
        col_num = len(title)
        # print("col_num: ", col_num)
        count = 0
        flag = True
        while flag:
            with database.batch() as batch:
                for _ in range(batch_size):

                    try:
                        item = next(reader)

                        assign_values = handle_row_for_positive_cover(item, col_num, title)
                        batch.insert_or_update(table=table_name, columns=cols, values=assign_values)

                        print(assign_values)
                    except StopIteration:
                        flag = False
                        break

                    count = count + 1
                    print(count)

