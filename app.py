import streamlit as st

from vector_search.vector_search import search


st.title("Поиск песни по фразе")
query = st.text_input("Введите фразу для поиска:")
print(query)
if query:
    st.subheader("Результаты поиска:")
    print(query)
    results = search(query)
    if results:
        for result in results:
            st.markdown(
                f"**Индекс:** {result['doc_id']} | **Ссылка:** [{result['link']}]"
                f"({result['link']}) | **Косинусное сходство:** {result['cosine_sim']:.2f}")
    else:
        st.write("По вашему запросу ничего не найдено.")
