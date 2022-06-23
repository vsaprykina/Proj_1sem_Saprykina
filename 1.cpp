class Point3d {
private:
    int m_x;
    int m_y;
    int m_z;

public:
    Point3d() {}
    Point3d(int m_x, int m_y, int m_z) {
        this->m_x = m_x;
        this->m_y = m_y;
        this->m_z = m_z;
        print_point();
    }
    void SetValues() {
    cout << "Введите координату x:";
    cin >> m_x;
    cout << "Введите координату y:";
    cin >> m_y;
    cout << "Введите координату z:";
    cin >> m_z;
    }
    void print_point() {
        cout << m_x << " " << m_y << " " << m_z << endl;
    }
};
int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    Point3d print;
    print.SetValues();
    print.print_point();
    return 0;
}
