package dao;

import dto.Product;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

public class ProductRepository {

    @Autowired
    SqlSession sqlSession;

    public List<Product> doSelect(){
        return sqlSession.selectList("product.select");

    }
    public void doInsert(Product product) {
        sqlSession.insert("product.insert",product);
    }
    public Product doSelectRow(Product product){
        sqlSession.selectOne("");
    }
}
