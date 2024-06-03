import streamlit as st # type: ignore

def hello_word():
    return "Olá, Turma de Dados! Aula de Docker"

def main():
    st.write(hello_word())

if __name__ == "__main__":
    main()