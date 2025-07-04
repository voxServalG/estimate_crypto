import numpy as np
import pandas as pd

# 设置 pandas 的显示选项，以便能看清所有列
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def inspect_dataset(file_path):
    """
    加载并探查 .npy 格式的数据集文件。
    """
    try:
        # 加载 .npy 文件。代码中的 .item() 表明其内容是一个字典。
        data_dict = np.load(file_path, allow_pickle=True).item()
        print(f"✅ 成功加载数据文件: {file_path}")
        print("-" * 70)

        # 检查加载的数据是否为字典
        if not isinstance(data_dict, dict):
            print(f"⚠️ 警告: 文件内容不是一个字典 (dictionary)，而是一个 {type(data_dict)}。")
            print("数据内容:")
            print(data_dict)
            return

        # 获取所有交易对/股票代码
        symbols = list(data_dict.keys())
        print(f"📊 数据集包含 {len(symbols)} 个交易对/股票。")
        print(f"部分代码示例: {symbols[:5]}")
        print("-" * 70)

        # 选取第一个代码作为样本进行深入查看
        if symbols:
            sample_symbol = symbols[0]
            print(f"🔍 查看第一个交易对 '{sample_symbol}' 的数据格式和样本:")
            
            sample_df = data_dict[sample_symbol]
            
            if isinstance(sample_df, pd.DataFrame):
                print("数据类型: pandas DataFrame")
                print("\n字段 (Columns):", list(sample_df.columns))
                print("\n数据前5行:")
                print(sample_df.head())
            else:
                print(f"⚠️ 警告: '{sample_symbol}' 的数据不是 pandas DataFrame，而是 {type(sample_df)}。")

    except FileNotFoundError:
        print(f"❌ 错误: 找不到文件 '{file_path}'。请确保路径正确，并从项目根目录运行此脚本。")
    except Exception as e:
        print(f"❌ 加载或处理文件时发生错误: {e}")

if __name__ == '__main__':
    # 根据项目代码，数据文件路径很可能是这个
    dataset_path = './src/data/US/sp500/baseline_data_sp500.npy'
    inspect_dataset(dataset_path)